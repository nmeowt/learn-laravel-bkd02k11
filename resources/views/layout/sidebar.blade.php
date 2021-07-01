<div class="sidebar" data-active-color="rose" data-background-color="black">
    <div class="logo">
        <a href="http://www.creative-tim.com" class="simple-text logo-mini">
            BK
        </a>
        <a href="http://www.creative-tim.com" class="simple-text logo-normal">
            D02K11
        </a>
    </div>
    <div class="sidebar-wrapper">
        <ul class="nav">
            <li class="{{ Request::is('/') ? 'active' : '' }}">
                <a href="{{ route('dashboard') }}">
                    <i class="material-icons">dashboard</i>
                    <p> Dashboard </p>
                </a>
            </li>
            <li class="{{ Request::is('grade') ? 'active' : '' }}">
                <a href=" {{ route('grade.index') }}">
                    <i class="material-icons">widgets</i>
                    <p> Quản lý lớp </p>
                </a>
            </li>
            <li class="{{ Request::is('student') ? 'active' : '' }}">
                <a href=" {{ route('student.index') }}">
                    <i class="material-icons">assignment</i>
                    <p> Quản lý sinh viên </p>
                </a>
            </li>
            <li>
                <a href="./charts.html">
                    <i class="material-icons">timeline</i>
                    <p> Charts </p>
                </a>
            </li>
            <li>
                <a href="./calendar.html">
                    <i class="material-icons">date_range</i>
                    <p> Calendar </p>
                </a>
            </li>
        </ul>
    </div>
</div>
