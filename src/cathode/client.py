from __future__ import annotations

import httpx

from cathode.exceptions import APIError, AuthenticationError, NotFoundError


class CathodeClient:
    """Cathode Cloud API client."""

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str = "https://api.cathode.cloud",
        timeout: float = 30.0,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self._api_key = api_key
        self._http = httpx.Client(
            base_url=self.base_url,
            timeout=timeout,
            headers=self._build_headers(),
        )

    def _build_headers(self) -> dict[str, str]:
        headers: dict[str, str] = {"User-Agent": "cathode-python"}
        if self._api_key:
            headers["Authorization"] = f"Bearer {self._api_key}"
        return headers

    def _request(self, method: str, path: str, **kwargs) -> dict:
        response = self._http.request(method, path, **kwargs)
        if response.status_code == 401:
            raise AuthenticationError("Invalid or missing API key")
        if response.status_code == 404:
            raise NotFoundError(f"Resource not found: {path}")
        if response.status_code >= 400:
            raise APIError(f"API error {response.status_code}: {response.text}")
        return response.json()

    def get(self, path: str, **kwargs) -> dict:
        return self._request("GET", path, **kwargs)

    def post(self, path: str, **kwargs) -> dict:
        return self._request("POST", path, **kwargs)

    def put(self, path: str, **kwargs) -> dict:
        return self._request("PUT", path, **kwargs)

    def delete(self, path: str, **kwargs) -> dict:
        return self._request("DELETE", path, **kwargs)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> CathodeClient:
        return self

    def __exit__(self, *args) -> None:
        self.close()
