from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import xmltodict

app = FastAPI()

@app.post("/parse-xml")
async def parse_xml(request: Request):
    try:
        xml_data = await request.body()
        parsed_data = xmltodict.parse(xml_data.decode('utf-8'))
        return JSONResponse(content={"success": True, "data": parsed_data})
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error parsing XML: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)