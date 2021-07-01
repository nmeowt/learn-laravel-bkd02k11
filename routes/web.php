<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\GradeController;
use App\Http\Controllers\StudentController;
use App\Http\Controllers\AuthenticateController;
use App\Http\Middleware\CheckLogin;

// Route::method(uri, action);

// Authentication
// Tạo middleware CheckLogged: nếu đăng nhập rồi thì quay về trang dashboard còn chưa thì ok
Route::get('/login', [AuthenticateController::class, 'login'])->name('login');
Route::post('/login-process', [AuthenticateController::class, 'loginProcess'])->name('login-process');


Route::middleware([CheckLogin::class])->group(function () {
    Route::get('/', function () {
        return view('dashboard');
    })->name('dashboard');

    Route::get('/logout', [AuthenticateController::class, 'logout'])->name('logout');

    # Tạo route sinh viên in ra Chào các bạn bằng controller
    Route::get('/student/{name}', [StudentController::class, 'getName']);

    // Thêm lớp
    Route::resource("grade", GradeController::class);
});
