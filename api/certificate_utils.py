import base64,os

def decode_certificate(input_file_path,output_file_path):
    with open(input_file_path, 'r') as file:
        encoded_secret = file.read().strip()  # Read the base64-encoded value
        decoded_secret = base64.b64decode(encoded_secret).decode("utf-8")  # Decode the base64 secret value
        
    
        with open(output_file_path, 'w') as output_file:
            output_file.write(decoded_secret)
            print("hello...")
            print(decoded_secret)

if __name__=="__main__":
   decode_certificate('client-cert/base64_encoded_client.pem','client-cert-dec/CLIENT.pem')
   decode_certificate('client-cert/base64_encoded_clientkey.pem','client-cert-dec/CLIENTKEY.pem')
