from typing import Annotated, Optional

import typer

from git_object import ObjectTypes, cat_file
from git_repository import repo_create
from git_utils import repo_find

app = typer.Typer()


def cmd_add(args):
    pass


@app.command()
def cat_file(object: ObjectTypes, type: str):
    repo = repo_find()
    cat_file(repo, object, fmt=type.encode())


def cmd_check_ignore(args):
    pass


def cmd_checkout(args):
    pass


def cmd_commit(args):
    pass


def cmd_hash_object(args):
    pass


@app.command()
def init(path: str):
    repo_create(path)


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


def main():
    app()
    # TODO: Configure pylint / mypy
    # TODO: https://typer.tiangolo.com/tutorial/subcommands/single-file/
