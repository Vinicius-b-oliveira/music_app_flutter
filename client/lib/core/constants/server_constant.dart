import 'dart:io';

class ServerConstant {
  static String serverURL =
      Platform.isAndroid
          ? 'https://7255-200-192-64-65.ngrok-free.app'
          : 'http://127.0.0.1:8000';
}
