# app.py — tema/estilo igual ao Extrator + mesma lógica do seu detector
import gradio as gr
from pathlib import Path
from detector import processar_misto, resumo_formatos  # usa seu pipeline

# ------------------- Tema + CSS (escuro, sem rodapé) -------------------
CUSTOM_CSS = """
:root{
  --bg:#000;
  --panel:#0b0b0b;
  --panel-2:#0e0e0e;
  --border:#2a2a2a;
  --text:#e5e5e5;
  --muted:#a3a3a3;
  --accent:#6ee7b7;
}
html, body, .gradio-container {
  background: var(--bg)!important;
  color: var(--text)!important;
  font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Inter, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif !important;
}
.gradio-container .block,
.gradio-container .gr-box,
.gradio-container .gr-panel {
  background: var(--panel) !important;
  border: 1px solid var(--border) !important;
  border-radius: 12px !important;
}
/* título sem caixa atrás */
.gradio-container .block:has(h1){
  background: transparent !important; border:0 !important; box-shadow:none !important;
}
/* botões estilo pílula */
button, .gr-button{
  border-radius:9999px !important; border:1px solid var(--border) !important; background: var(--panel-2) !important;
}
button:hover{ border-color:#4a4a4a !important; }
/* inputs/áreas de texto/select */
input, textarea, select,
.gradio-container .gr-textbox,
.gradio-container .gr-input,
.gradio-container .gradio-dropdown,
.gradio-container .gr-file,
.gradio-container .gr-file-download {
  background: var(--panel-2) !important;
  border: 1px solid var(--border) !important;
  color: var(--text) !important;
  border-radius: 12px !important;
}
.gradio-container textarea { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
/* foco visível */
input:focus, textarea:focus, select:focus,
.gradio-container .gr-textbox:focus-within,
.gradio-container .gr-input:focus-within,
.gradio-container .gradio-dropdown:focus-within,
.gradio-container .gr-file:focus-within {
  outline: none !important;
  border-color: var(--accent) !important;
  box-shadow: 0 0 0 2px rgba(110,231,183,0.18) !important;
}
/* esconder badges de rodapé */
.gradio-container .fixed.bottom-0,
.gradio-container footer,
body > div.fixed.bottom-0 { display:none !important; visibility:hidden !important; height:0 !important; overflow:hidden !important; }
"""

THEME = gr.themes.Soft(primary_hue="zinc", neutral_hue="zinc")

# ------------------------- Utilitário -------------------------
def _paths_from_files(file_list):
  if not file_list: return []
  if isinstance(file_list, str): return [Path(file_list)]
  return [Path(p) for p in file_list]

# ---------------------- Função principal ----------------------
def executar(arquivos, gerar_csv):
  paths = _paths_from_files(arquivos)
  if not paths:
    return "Envie ao menos 1 arquivo (pode ser .zip).", "", None

  zip_path, relatorio, counts = processar_misto(paths, gerar_csv=gerar_csv)

  # Relatório detalhado por arquivo
  linhas = [
    "arquivo_original  →  saída  (ext_detectada)",
    "-" * 60,
  ]
  for a, b, c in relatorio:
    linhas.append(f"{a:30} →  {b:30} ({c or '—'})")
  relatorio_txt = "\n".join(linhas)

  # Resumo amigável
  resumo_txt = resumo_formatos(counts)
  return relatorio_txt, resumo_txt, zip_path

# ------------------------- Interface --------------------------
demo = gr.Interface(
  fn=executar,
  inputs=[
    gr.Files(
      label="Envie arquivo(s) (aceita arquivo único, vários e/ou .zip)",
      file_count="multiple",
    ),
    gr.Checkbox(label="Gerar CSV também (além do Excel)", value=False),
  ],
  outputs=[
    gr.Textbox(label="Relatório por arquivo", lines=14, show_copy_button=True),
    gr.Textbox(label="Resumo por formato", lines=12, show_copy_button=True),
    gr.File(label="Download do .zip processado"),
  ],
  title="Renomeador por Assinatura de Arquivo (Magic Number)",
  allow_flagging="never",
  theme=THEME,
  css=CUSTOM_CSS,
)

if __name__ == "__main__":
  demo.launch()
