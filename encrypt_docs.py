import os
import subprocess
from pathlib import Path


def encrypt_docs():
    # Diretório dos arquivos gerados pelo MkDocs
    site_dir = Path("site")
    password = os.environ.get("DOCS_PASSWORD", "sua-senha-aqui")
    template = Path("docs/overrides/password.html")

    # Percorre todos os arquivos HTML no diretório site
    for html_file in site_dir.rglob("*.html"):
        print(html_file)
        if html_file.name != "password.html":
            try:
                subprocess.run(
                    [
                        "npx",
                        "staticrypt",
                        str(html_file),
                        password,
                        "--template",
                        str(template),
                        "--remember-password",
                        "--output",
                        str(html_file),
                    ],
                    check=True,
                )
                print(f"Encrypted: {html_file}")

            except subprocess.CalledProcessError as e:
                print(f"Error encrypting {html_file}: {e}")


if __name__ == "__main__":
    encrypt_docs()
