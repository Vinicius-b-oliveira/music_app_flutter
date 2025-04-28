import 'dart:io';

class ServerConstant {
  static String serverURL =
      Platform.isAndroid
          ? 'https://b60f-45-163-74-66.ngrok-free.app'
          : 'http://127.0.0.1:8000';
}
