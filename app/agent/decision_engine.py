def decide_action(state):
    if state["bank_status"] == "success" and state["gateway_status"] != "success":
        return "INITIATE_REFUND"

    if state["sentiment"] == "angry":
        return "ESCALATE"

    return "EXPLAIN"
