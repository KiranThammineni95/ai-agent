from tools import get_current_time, roll_dice, generate_password
def execute_tool(user_input):
    """Executes a tool based on the user's input."""
    user_text = user_input.lower()

    if "time" in user_text or "clock" in user_text:
        return get_current_time()

    if "dice" in user_text or "roll the dice" in user_text:
        return f"You rolled: {roll_dice()}"

    if "password" in user_text:
        return generate_password()

    return None