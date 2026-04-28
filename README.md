# GITHUB ASSISTANT MCP
## Structure Project

```text
github-pr-assistant-mcp/
│
├── app/
│   ├── main.py              # FastAPI entrypoint
│   ├── config.py            # Variables de entorno
│   ├── routes/
│   │   └── github.py        # Endpoints API
│   ├── services/
│   │   ├── github_service.py
│   │   ├── analyzer.py
│   │   └── mcp_service.py
│   ├── models/
│   │   └── schemas.py
│   └── utils/
│       └── helpers.py
│
├── tests/
│
├── Dockerfile
├── requirements.txt
├── .env
├── .gitignore
└── README.md


# Resume

This project is a MCP that work with API Github, made pull request, analyst projesc PR´s, include mark if the Pull rquest is front, back, or other service, this MCP analyze the commits with the help API chatgpt