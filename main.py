from app.main import app

if __name__ == "__main__":
    import uvicorn
    print("==================================================================")
    print("  SIMULADOR DE EXÁMENES EDUCATIVOS (FASTAPI)")
    print("  Accede en tu navegador a: http://127.0.0.1:8000")
    print("==================================================================")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
