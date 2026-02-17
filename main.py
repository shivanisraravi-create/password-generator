import argparse
from generator.core import generate_password
from generator.validator import validate_password
from generator.entropy import calculate_entropy

def main():
    parser = argparse.ArgumentParser(description="Secure Password Generator")

    parser.add_argument("--length", type=int, default=16)
    parser.add_argument("--no-lower", action="store_true")
    parser.add_argument("--no-upper", action="store_true")
    parser.add_argument("--no-digits", action="store_true")
    parser.add_argument("--no-symbols", action="store_true")

    args = parser.parse_args()

    use_lower = not args.no_lower
    use_upper = not args.no_upper
    use_digits = not args.no_digits
    use_symbols = not args.no_symbols

    while True:
        password, charset_size = generate_password(
            length=args.length,
            use_lower=use_lower,
            use_upper=use_upper,
            use_digits=use_digits,
            use_symbols=use_symbols
        )

        if validate_password(password, use_lower, use_upper, use_digits, use_symbols):
            break

    entropy = calculate_entropy(args.length, charset_size)

    print("\nGenerated Password:", password)
    print("Entropy:", entropy, "bits")

if __name__ == "__main__":
    main()
