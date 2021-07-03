<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\GradeController;
use App\Http\Controllers\StudentController;
use App\Http\Controllers\AuthenticateController;
use App\Http\Middleware\CheckLogin;
use App\Mail\TestMail;
use Illuminate\Support\Facades\Mail;

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

    // lớp
    Route::resource("grade", GradeController::class);

    // sinh viên
    Route::resource("student", StudentController::class);
    Route::prefix("student")->name('student.')->group(function () {
        Route::get('hide/{id}', [StudentController::class, 'hide'])->name('hide');
    });

    Route::get("/mail", function () {
        Mail::to("yahoo@gmail.com")->send(new TestMail());
    });
});
