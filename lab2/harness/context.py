from pathlib import Path
 
 
ALLOWED_EXTENSIONS = {
    ".py",
    ".md",
    ".txt",
    ".json",
    ".toml",
    ".yaml",
    ".yml",
}
 
 
def collect_repository_context(
    project_path: Path,
    max_characters: int = 12_000,
) -> str:
    sections: list[str] = []
    current_size = 0
 
    for path in sorted(project_path.rglob("*")):
        if not path.is_file():
            continue
 
        if path.suffix not in ALLOWED_EXTENSIONS:
            continue
 
        if ".venv" in path.parts or "__pycache__" in path.parts:
            continue
 
        relative_path = path.relative_to(project_path)
 
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
 
        section = (
            f"\n--- FILE: {relative_path} ---\n"
            f"{content}\n"
        )
 
        if current_size + len(section) > max_characters:
            break
 
        sections.append(section)
        current_size += len(section)

    return "".join(sections)


def is_path_inside_repository(
    path: Path,
    repository_root: Path,
) -> bool:
    try:
        path.resolve().relative_to(repository_root.resolve())
        return True
    except ValueError:
        return False



def is_path_inside_repository(
    path: Path,
    repository_root: Path,
) -> bool:
    try:
        path.resolve().relative_to(repository_root.resolve())
        return True
    except ValueError:
        return False