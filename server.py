from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 국토부 API 호출
@app.route('/get-building-info', methods=['GET'])
def get_building_info():
    service_key = "MrVDw1GpFYZDIUkjsa8GHTTzfiy9H8CVSKLe8otH2cQmSnzbaQYnUC5TCrXBXQghAVe49Fcj60zCwXa35XB2xw=="
    
    params = {
        "serviceKey": service_key,
        "sigunguCd": request.args.get("sigunguCd"),
        "bjdongCd": request.args.get("bjdongCd"),
        "platGbCd": request.args.get("platGbCd"),
        "bun": request.args.get("bun"),
        "ji": request.args.get("ji"),
        "numOfRows": "10",
        "pageNo": "1",
        "_type": "json"
    }

    api_url = "https://apis.data.go.kr/1613000/BldRgstHubService/getBrTitleInfo"

    try:
        response = requests.get(api_url, params=params, verify=False)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
