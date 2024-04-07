import argparse
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def install(args):
    logger.info("Installing dotfiles")
    logger.debug(
        f"installing dotfiles from {args.repo} with link={args.link}, force={args.force}, dry_run={args.dry_run}, skip_existing={args.skip_existing}")


def update(args):
    logger.info("Updating dotfiles")
    logger.debug(f"Updating dotfiles with dry_run={args.dry_run}")


def main():
    parser = argparse.ArgumentParser(description="A simple dotfiles manager for Linux written in Python by kedar")
    subparsers = parser.add_subparsers()

    # Install subcommand
    install_parser = subparsers.add_parser('install', help='Install dotfiles')
    install_parser.set_defaults(func=install)
    install_parser.add_argument("repo", help="Repository URL")
    install_parser.add_argument("-l", "--link", action="store_true", help="Link dotfiles instead of copying")
    install_parser.add_argument("-f", "--force", action="store_true",
                                help="Force install even if dotfiles already exist")
    install_parser.add_argument("--dry-run", action="store_true",
                                help="Show what will be installed without actually installing")
    install_parser.add_argument("--skip-existing", action="store_true", help="Skip existing files")

    # Update subcommand
    update_parser = subparsers.add_parser('update', help='Update dotfiles')
    update_parser.set_defaults(func=update)
    update_parser.add_argument("--dry-run", action="store_true",
                               help="Show what will be updated without actually updating")

    # Help subcommand
    help_parser = subparsers.add_parser('help', help='Show help')
    help_parser.set_defaults(func=parser.print_help)

    # Debug logging
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")

    args = parser.parse_args()
    if args.debug:
        logger.setLevel(logging.DEBUG)

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
