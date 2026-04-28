# cathode-sdk

Python SDK & CLI for [Cathode Cloud](https://cathode.cloud).

## Install

```bash
pip install cathode
```

## SDK Usage

```python
from cathode import CathodeClient

with CathodeClient(api_key="your-api-key") as client:
    response = client.get("/v1/me")
    print(response)
```

## CLI Usage

```bash
export CATHODE_API_KEY="your-api-key"

cathode whoami
```

## Development

```bash
pip install -e ".[dev]"
pytest
ruff check .
```

## License

MIT
