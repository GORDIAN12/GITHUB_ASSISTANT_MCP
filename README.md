# GITHUB ASSISTANT MCP

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