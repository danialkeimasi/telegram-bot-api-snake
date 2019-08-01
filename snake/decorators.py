from functools import wraps
import yaml
import attrdict

config = attrdict.AttrDict(yaml.safe_load(open("./config.yml", 'r')))

def send_action(action):
    """Sends `action` while processing func command."""

    def decorator(func):
        @wraps(func)
        def command_func(bot, update, *args, **kwargs):
            bot.send_chat_action(chat_id=update.effective_message.chat_id, action=action)

            return func(update, context,  *args, **kwargs)
        return command_func
    return decorator


def admin_only(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in config.bot.admins:
            print("Unauthorized access denied for {}.".format(user_id))
            return

        return func(update, context, *args, **kwargs)
    return wrapped
