---
title: Renomeador por Assinatura (Magic Number)
emoji: 🧪
colorFrom: gray
colorTo: gray
sdk: gradio
sdk_version: "4.0.0"
app_file: app.py
pinned: false
---

Detecção de extensões por *magic number* + heurísticas (ZIP, Office, APK/JAR, etc).
Gera **XLSX formatado** e **CSV opcional**. Envie vários arquivos e/ou **.zip** em uma vez.

### Como usar
1) Solte arquivos e/ou `.zip` na caixa.  
2) (Opcional) Marque “Gerar CSV”.  
3) Clique **Submit**. Baixe o `.zip processado`.

### Saídas
- `relatorio_renomeacao.xlsx` (sempre)  
- `relatorio_renomeacao.csv` (se marcado)  
- Arquivos copiados/renomeados com a extensão detectada.

> Observação: arquivos já com extensão “conhecida” não são renomeados.
