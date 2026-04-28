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

def checklist_pr(files):
    names = [file["filename"].lower() for file in files]

    backend = any(
        name.endswith(".py") or "api" in name or "server" in name
        for name in names
    )

    frontend = any(
        name.endswith(".js") or name.endswith(".html") or name.endswith(".css")
        for name in names
    )

    tests = any("test" in name for name in names)

    docs = any(
        name.endswith(".md") or "readme" in name
        for name in names
    )

    config = any(
        ".env" in name or "dockerfile" in name or ".yml" in name
        for name in names
    )

    recommendation = "Checklist completa."

    if not tests:
        recommendation = "Faltan tests para este cambio."

    return {
        "backend": backend,
        "frontend": frontend,
        "tests": tests,
        "docs": docs,
        "config": config,
        "recommendation": recommendation
    }