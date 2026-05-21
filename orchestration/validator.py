REQUIRED_FIELDS = [
    "Feedback_ID",
    "Main_Category",
    "Customer_Sentiment",
    "Issue_Summary",
    "Order_Reference_ID",
    "Product_Reference",
    "Suggested_Department",
    "Actionable_Resolution_Points"
]


def validate_response(response: dict) -> bool:
    """
    Validates that all required JSON fields exist.
    """

    for field in REQUIRED_FIELDS:
        if field not in response:
            return False

    return True
