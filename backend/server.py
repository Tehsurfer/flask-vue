from service.app import app

# For local development only
if __name__ == '__main__':
  app.run(debug=True, port=80)
