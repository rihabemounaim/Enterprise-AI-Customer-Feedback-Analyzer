import json

from prompt_loader import load_prompt
from llm_router import simulate_llm_response
from validator import validate_response
from department_router import route_to_department


def main():

    # Load prompt template
    prompt = load_prompt("../prompts/multi_issue_prompt_v3.txt")

    # Load customer email
    with open("sample_email.txt", "r", encoding="utf-8") as file:
        customer_email = file.read()

    # Inject email into prompt
    final_prompt = prompt.replace(
        "{{?user_email_placeholder}}",
        customer_email
    )

    print("=== PROMPT READY ===\n")

    # Simulated LLM response
    response = simulate_llm_response(customer_email)

    # Validate JSON structure
    is_valid = validate_response(response)

    if not is_valid:
        raise ValueError("Invalid JSON response")

    print("=== STRUCTURED RESPONSE ===\n")
    print(json.dumps(response, indent=2))

    # Route to business department
    routing = route_to_department(response)

    print("\n=== WORKFLOW RESULT ===")
    print(routing)


if __name__ == "__main__":
    main()
