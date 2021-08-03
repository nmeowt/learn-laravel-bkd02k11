<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

// admin
class Admin extends Model
{
    use HasFactory;
    protected $table = 'admin';

    public $timestamps = false;

    public $primaryKey = 'idAdmin';
}
