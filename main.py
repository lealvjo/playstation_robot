from flask import Flask, jsonify

from app.controller.playstation import ControllerPlaystation
from app.services.mercado_livre import BotMercadoLivre


def create_app():
    app = Flask(__name__)
    bot_mercado_livre = BotMercadoLivre()

    @app.route('/')
    def index():
        return jsonify({"Status": "Api treinamento"}), 200

    @app.route('/runbot/mercadolivre', methods=['GET'])
    def route_run_bot():
        bot_mercado_livre.captured_sales_collection()
        return jsonify({"Status": "Bot capturou os dados com sucesso"}), 200

    @app.route('/resultbot/mercadolivre', methods=['GET'])
    def route_result_bot():
        return jsonify(ControllerPlaystation.getter_products()), 200

    @app.route('/resultbotfuzzy/mercadolivre', methods=['GET'])
    def route_result_bot_fuzzy():
        return jsonify(ControllerPlaystation.getter_products_fuzzy()), 200

    return app


def main():
    create_app().run()


if __name__ == '__main__':
    main()
