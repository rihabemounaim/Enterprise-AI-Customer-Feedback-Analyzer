def route_to_department(response: dict) -> str:
    """
    Simulates enterprise workflow routing.
    """

    department = response.get("Suggested_Department", "Customer Service")

    return f"Ticket routed to: {department}"
