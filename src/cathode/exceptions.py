class CathodeError(Exception):
    """Base exception for all Cathode errors."""


class AuthenticationError(CathodeError):
    """Raised when authentication fails."""


class NotFoundError(CathodeError):
    """Raised when a resource is not found."""


class APIError(CathodeError):
    """Raised for general API errors."""
