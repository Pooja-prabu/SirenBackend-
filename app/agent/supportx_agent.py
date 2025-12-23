from app.agent.decision_engine import decide_action
from app.agent.tools import initiate_refund, escalate

def run_agent(state, db):
    decision = decide_action(state)

    if decision == "INITIATE_REFUND":
        return initiate_refund(state, db)

    if decision == "ESCALATE":
        return escalate(state)

    return {"message": "Issue explained to user."}
