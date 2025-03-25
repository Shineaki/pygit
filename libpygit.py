import argparse
import sys

from git_repository import repo_create


def cmd_add(args):
    pass


def cmd_cat_file(args):
    pass


def cmd_check_ignore(args):
    pass


def cmd_checkout(args):
    pass


def cmd_commit(args):
    pass


def cmd_hash_object(args):
    pass


def cmd_init(args):
    repo_create(args.path)


def cmd_log(args):
    pass


def cmd_ls_files(args):
    pass


def cmd_ls_tree(args):
    pass


def cmd_rev_parse(args):
    pass


def cmd_rm(args):
    pass


def cmd_show_ref(args):
    pass


def cmd_status(args):
    pass


def cmd_tag(args):
    pass


def main(argv=sys.argv[1:]):
    # TODO: Remove unused imports from all files
    # TODO: Configure pylint / flake8 / mypy / ruff
    # TODO: Replace all this crap with Typer - https://github.com/fastapi/typer
    argparser = argparse.ArgumentParser(description="The stupidest content tracker")
    argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
    argsubparsers.required = True
    argsp = argsubparsers.add_parser("init", help="Initialize a new, empty repository.")
    argsp.add_argument(
        "path",
        metavar="directory",
        nargs="?",
        default=".",
        help="Where to create the repository.",
    )
    argsp = argsubparsers.add_parser(
        "cat-file", help="Provide content of repository objects"
    )
    argsp.add_argument(
        "type",
        metavar="type",
        choices=["blob", "commit", "tag", "tree"],
        help="Specify the type",
    )

    argsp.add_argument("object", metavar="object", help="The object to display")
    args = argparser.parse_args(argv)
    match args.command:
        case "add":
            cmd_add(args)
        case "cat-file":
            cmd_cat_file(args)
        case "check-ignore":
            cmd_check_ignore(args)
        case "checkout":
            cmd_checkout(args)
        case "commit":
            cmd_commit(args)
        case "hash-object":
            cmd_hash_object(args)
        case "init":
            cmd_init(args)
        case "log":
            cmd_log(args)
        case "ls-files":
            cmd_ls_files(args)
        case "ls-tree":
            cmd_ls_tree(args)
        case "rev-parse":
            cmd_rev_parse(args)
        case "rm":
            cmd_rm(args)
        case "show-ref":
            cmd_show_ref(args)
        case "status":
            cmd_status(args)
        case "tag":
            cmd_tag(args)
        case _:
            print("Bad command.")
