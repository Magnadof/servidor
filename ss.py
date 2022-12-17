import logging
from telegram.ext import Updater, CommandHandler

# Ative o logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Defina a função que o bot irá executar quando receber um comando '/start'
def start(update, context):
    update.message.reply_text('Olá, mundo!')


def main():
    # Crie o Updater e passe o token do seu bot
    updater = Updater('5972106919:AAHKRWTGHNz27_uYs3l9ilkVLUkMMsVCxDk', use_context=True)

    # Obtenha o dispatcher para registrar os manipuladores
    dp = updater.dispatcher

    # Registre o manipulador para o comando '/start'
    dp.add_handler(CommandHandler('start', start))

    # Inicie o bot
    updater.start_polling()

    # Execute o bot até que você pressione Ctrl-C ou o processo receba um sinal de parada
    updater.idle()


if __name__ == '__main__':
    main()
