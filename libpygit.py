from typing import Annotated, Optional

import typer

from git_object import ObjectTypes, call_cat_file, object_hash
from git_repository import repo_create
from git_utils import repo_find

app = typer.Typer()


@app.command()
def init(path: str):
    repo_create(path)


@app.command()
def cat_file(object: ObjectTypes, type: str):
    repo = repo_find()
    call_cat_file(repo, object, fmt=type.encode())


@app.command()
def hash_object(
    path: str,
    write: Annotated[
        Optional[bool],
        typer.Option("-w", help="Actually write the object into the database"),
    ] = False,
    type: Annotated[
        Optional[ObjectTypes], typer.Option("-t", help="Specify the type")
    ] = ObjectTypes.blob,
):
    if write:
        repo = repo_find()
    else:
        repo = None

    with open(path, "rb") as fd:
        sha = object_hash(fd, type.encode(), repo)
        print(sha)


def cmd_add(args):
    pass


def cmd_check_ignore(args):
    pass


def cmd_checkout(args):
    pass


def cmd_commit(args):
    pass


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
