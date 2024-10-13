from loader import app
import handlers, uvicorn, logging



# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     handlers=[
#         logging.FileHandler("logfile.log"),
#         logging.StreamHandler()  # Still prints logs to terminal
#     ]
# )


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000)