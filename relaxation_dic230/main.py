import uvicorn


def run() -> None:
    uvicorn.run("relaxation_dic230.app:app", host="127.0.0.1", port=8000)


if __name__ == "__main__":
    run()
