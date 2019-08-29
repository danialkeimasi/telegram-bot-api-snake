import peewee

from snake import ChatAction, is_authenticated
from snake.decorators import debug, send_action
from . import pages, models


@send_action(ChatAction.TYPING)
def start(bot, update):
    try:
        models.User.create(
            chat_id=update.message.from_user.id,
            name=update.message.from_user.first_name,
        )

    except peewee.IntegrityError:
        update.message.reply_text('you are signed up before!')

    else:
        update.message.reply_text('you are signed up succesfully!')


@send_action(ChatAction.TYPING)
def message(bot, update):
    models.Activity.create(
        user_id=update.message.from_user.id,
        message=update.message.text
    )
    update.message.reply_text(f'you said "{update.message.text}".')


@send_action(ChatAction.TYPING)
def getme(bot, update):
    activities = models.Activity.filter(models.Activity.user_id == update.message.from_user.id).execute()
    message = 'you said theese messages:\n\n' + ''.join([f'- {activity.message}\n\n' for activity in activities])
    update.message.reply_text(message)


@send_action(ChatAction.TYPING)
def clear(bot, update):
    delete_result = models.Activity.delete().where(models.Activity.user_id == update.message.from_user.id).execute()
    update.message.reply_text(f'your activity is cleared!\ndeleted {delete_result}')
