from functools import wraps

import attrdict
import yaml
from telegram import ChatAction

config = attrdict.AttrDict(yaml.safe_load(open("./config.yml", 'r')))


def send_action(action):
    """Sends `action` while processing func command."""

    def decorator(func):
        @wraps(func)
        def command_func(bot, update, *args, **kwargs):
            bot.send_chat_action(chat_id=update.effective_message.chat_id, action=action)

            return func(bot, update, *args, **kwargs)

        return command_func

    return decorator


def admin_only(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in config.bot.admins:
            print("Unauthorized access denied for {}.".format(user_id))
            return

        return func(bot, update, *args, **kwargs)

    return wrapped


send_typing_action = send_action(ChatAction.TYPING)
send_upload_video_action = send_action(ChatAction.UPLOAD_VIDEO)
send_upload_photo_action = send_action(ChatAction.UPLOAD_PHOTO)

# FIND_LOCATION
# RECORD_AUDIO
# RECORD_VIDEO
# RECORD_VIDEO_NOTE
# UPLOAD_AUDIO
# UPLOAD_DOCUMENT
# UPLOAD_PHOTO
# UPLOAD_VIDEO
# UPLOAD_VIDEO_NOTE
