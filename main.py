from flask import Flask, jsonify
from app.bots.mercado_livre import botMercadoLivre


def create_app():
    app = Flask(__name__)
    bot_mercado_livre = botMercadoLivre()

    @app.route('/')
    def index():
        return jsonify({"Status": "Api treinamento"}), 200

    @app.route('/runbot', methods=['GET'])
    def route_run_bot():
        bot_mercado_livre.captured_sales_collection()
        return jsonify({"Status": "Bot capturou os dados com sucesso"}), 200

    @app.route('/resultbot', methods=['GET'])
    def route_result_bot():
        return jsonify(bot_mercado_livre.getter_products()), 200

    return app


def main():
    create_app().run()


if __name__ == '__main__':
    main()
