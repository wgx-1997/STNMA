from stnma import STNMA
from utils import parameter_parser, args_printer


def main():
    args = parameter_parser()
    args_printer(args)

    stnma = STNMA(args)
    stnma.fit()


if __name__ == '__main__':
    main()
