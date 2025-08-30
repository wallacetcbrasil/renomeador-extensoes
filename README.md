# Renomeador por Assinatura (Magic Number)

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Gradio](https://img.shields.io/badge/Gradio-4.x-FF6F61)](https://www.gradio.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Detecta a **extensão real** de arquivos pela assinatura (magic number) e por **heurísticas** (ex.: ZIP → DOCX/XLSX/PPTX, APK/JAR etc.).  
Gera **relatório XLSX** (formatado) e, opcionalmente, **CSV**. Aceita **vários arquivos** e/ou um **.zip** com muitos arquivos de uma vez.

> Interface em **Gradio 4** com tema escuro padronizado (mesma identidade visual do portfólio).

---

## ✨ Recursos

- **Detecção por assinatura** (magic bytes) + **heurísticas** para contêineres ZIP (Office, APK/JAR…)
- **Entrada múltipla**: arquivos soltos e/ou um **.zip**
- **Relatórios**: `relatorio_renomeacao.xlsx` (sempre) e `relatorio_renomeacao.csv` (opcional)
- **Resumo por formato** (contagem de detectados/ajustados)
- **Download** de um **.zip processado** com os arquivos de saída + relatórios

---

## 🖼️ Demonstração

- **Hugging Face Space:** _(adicione aqui a URL quando publicar)_
- **Portfólio:** _(adicione aqui o link do card no seu site)_

---

## 🧠 Como funciona (resumo técnico)

1. Para cada arquivo, detecta o tipo real por **magic number**.  
2. Em formatos contêiner (ex.: ZIP), aplica **heurísticas** (ex.: presença de pastas/arquivos típicos de DOCX/XLSX/PPTX, APK, JAR…).  
3. Se necessário, **renomeia** (ou apenas **copia**) com a extensão correta.  
4. Gera **XLSX** (com formatação) e, se marcado, **CSV**.  
5. Entrega tudo em um **.zip** para download.

> Arquivos cuja extensão já condiz com a detecção **não são renomeados**.

---

## 📦 Requisitos

- **Python 3.10+**
- Pacotes (pip): `gradio>=4.0.0`, `openpyxl`

`requirements.txt`:
```txt
gradio>=4.0.0
openpyxl