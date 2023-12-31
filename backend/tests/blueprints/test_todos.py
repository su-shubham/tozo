from quart import Quart


async def test_post_todo(app: Quart) -> None:
    test_client = app.test_client()
    async with test_client.authenticated("1"):
        response = await test_client.post(
            "/todos/",
            json={"complete": False, "due": None, "task": "Test task"},
        )
        assert response.status_code == 201
        assert (await response.get_json())["id"] > 0

    # test_client = app.test_client()
    # async with test_client.authenticated("1"):
    #     response = await test_client.post("/todos/",json={"task":"Test Task","complete":False,"due":None})
    #     assert response.status_code == 201
    #     assert(await response.get_json())["id"] > 0 

async def test_get_todo(app: Quart) -> None:
    test_client = app.test_client()
    async with test_client.authenticated("1"):  # type: ignore
        response = await test_client.get("/todos/1/")
        assert response.status_code == 200
        assert (await response.get_json())["task"] == "Test Task"
