async def health_check():
    return {"status": "ok"}


__all__ = ["health_check"]
