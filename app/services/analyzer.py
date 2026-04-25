def analyze_pr(data):
    title = data["title"]
    files = data["changed_files"]
    body = data["body"] or ""

    summary = f"El PR '{title}' modifica {files} archivo(s)."

    if ".gitignore" in body.lower() or "gitignore" in title.lower():
        impact = "Mejora la limpieza del repositorio y evita subir archivos innecesarios."
    else:
        impact = "Actualiza el proyecto con nuevos cambios."

    return {
        "summary": summary,
        "impact": impact,
        "files_changed": files,
        "status": data["state"]
    }