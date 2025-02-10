import requests

def delete_webhook(webhook_url):
    try:
        response = requests.delete(webhook_url, timeout=1)
        if response.status_code == 204:
            print("Webhook başarıyla silindi!")
        else:
            print(f"Webhook silinirken bir hata oluştu: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"API isteği sırasında bir hata oluştu: {e}")

# Komut satırından kullanıcıdan URL alma
webhook_url = input("Webhook URL'sini buraya yazın: ")
delete_webhook(webhook_url)
