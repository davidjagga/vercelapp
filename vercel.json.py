{
    "builds": [
        {
            "src":"api/app.py",
            "use":"@vercel/python"
        }
    ],
    "routes": [
        {
            "src":"/(.*)",
            "dest":"api/main.py"
        }
    ]
}