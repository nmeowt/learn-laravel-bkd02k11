<?php

use App\Http\Controllers\StudentController;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\GradeController;

// Route::method(uri, action);

# Tạo route sinh viên in ra Chào các bạn bằng controller
Route::get('/student/{name}', [StudentController::class, 'getName']);

// Thêm lớp
// Route::get("/grade/create", [GradeController::class, 'create']);
// Route::post("/grade/store", [GradeController::class, 'store'])->name('store');
Route::resource("grade", GradeController::class);

Route::get('/', function () {
    return view('dashboard');
})->name('dashboard');
