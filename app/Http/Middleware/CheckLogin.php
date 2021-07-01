<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Redirect;

class CheckLogin
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @return mixed
     */
    public function handle(Request $request, Closure $next)
    {
        // Nếu có tồn tại session
        if ($request->session()->exists('id')) {
            return $next($request);
        } else {  // Ngược lại không tồn tại
            return Redirect::route('login')->with('error', 'Chưa đăng nhập đâuuuu');
        }
    }
}
