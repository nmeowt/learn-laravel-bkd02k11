<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Grade extends Model
{
    protected $table = 'grade';
    public $timestamps = false;
    public $primaryKey = 'idGrade';
}
