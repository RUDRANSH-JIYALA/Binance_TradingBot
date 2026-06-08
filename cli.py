import argparse

from bot.orders import (
    place_market_order,
    place_limit_order
)

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.logging_config import logger


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True
    )

    parser.add_argument(
        "--side",
        required=True
    )

    parser.add_argument(
        "--type",
        required=True
    )

    parser.add_argument(
        "--quantity",
        required=True
    )

    parser.add_argument(
        "--price"
    )

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        print("\n===== ORDER REQUEST =====")
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        if order_type == "LIMIT":

            price = validate_price(args.price)

            print(f"Price    : {price}")

            response = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        else:

            response = place_market_order(
                symbol,
                side,
                quantity
            )

        print("\n===== ORDER RESPONSE =====")

        print(
            f"Order ID     : "
            f"{response.get('orderId')}"
        )

        print(
            f"Status       : "
            f"{response.get('status')}"
        )

        print(
            f"Executed Qty : "
            f"{response.get('executedQty')}"
        )

        print(
            f"Avg Price    : "
            f"{response.get('avgPrice')}"
        )

        print("\nSUCCESS: Order placed successfully")

    except Exception as e:

        logger.error(str(e))

        print(f"\nFAILED: {e}")


if __name__ == "__main__":
    main()
