from app.app import app
from app.routes import render_page_content
from app.pages.table import callbacks


if __name__ == '__main__':
    app.run_server(debug=True)

# %%
