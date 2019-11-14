# Generated by Django 2.1.1 on 2018-11-27 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpLeaveRequest',
            fields=[
                ('EmpLeave_Req_ID', models.PositiveIntegerField(default=0, primary_key=True, serialize=False)),
                ('Emp_FullName', models.CharField(max_length=50)),
                ('Leave_Type', models.CharField(choices=[('Personal_Leave', 'Personal'), ('Annual_Leave', 'Annual'), ('Military_Leave', 'Military'), ('Pregnancy_Disability_Leave', 'PDL'), ('Pending_Status', 'Pending'), ('Approved_Status', 'Approved'), ('Declined_Status', 'Declined')], max_length=10)),
                ('Manager_FullName', models.CharField(max_length=50)),
                ('Begin_Date', models.DateField(help_text='Leave begin date')),
                ('End_Date', models.DateField(help_text='Leave end date')),
                ('Requested_Days', models.PositiveIntegerField(default=0, help_text='Total no of requested leave days')),
                ('Leave_Status', models.CharField(choices=[('Personal_Leave', 'Personal'), ('Annual_Leave', 'Annual'), ('Military_Leave', 'Military'), ('Pregnancy_Disability_Leave', 'PDL'), ('Pending_Status', 'Pending'), ('Approved_Status', 'Approved'), ('Declined_Status', 'Declined')], max_length=10)),
                ('Emp_Comments', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Emp_No', models.PositiveIntegerField(default=0, help_text='Unique Emp no for employee table', primary_key=True, serialize=False)),
                ('First_Name', models.CharField(help_text='employee first name', max_length=14)),
                ('Middle_Name', models.CharField(help_text='employee middle name', max_length=14, null=True)),
                ('Last_Name', models.CharField(help_text='employee last name', max_length=14)),
                ('Birth_Date', models.DateField(help_text='employee birth date')),
                ('Gender', models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Employee', 'Employee'), ('Manager', 'Manager'), ('HR', 'HR'), ('Permanent', 'Permanent'), ('Probationary', 'Probationary'), ('Limited_term', 'Limited-term'), ('Temporary', 'Temporary')], max_length=1)),
                ('Street_Address', models.CharField(max_length=50)),
                ('Address2', models.CharField(max_length=50, null=True)),
                ('City', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=20)),
                ('Postal_Code', models.PositiveIntegerField(default=0)),
                ('Country', models.CharField(max_length=20)),
                ('Mobile_Number', models.PositiveIntegerField(default=0)),
                ('Email_Address', models.EmailField(max_length=70)),
                ('Hire_Date', models.DateField(help_text='Employee joining date')),
                ('End_Date', models.DateField(help_text='Employee last working date in organization', null=True)),
                ('Designation', models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Employee', 'Employee'), ('Manager', 'Manager'), ('HR', 'HR'), ('Permanent', 'Permanent'), ('Probationary', 'Probationary'), ('Limited_term', 'Limited-term'), ('Temporary', 'Temporary')], max_length=10)),
                ('Nationality', models.CharField(max_length=50)),
                ('Worktype', models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Employee', 'Employee'), ('Manager', 'Manager'), ('HR', 'HR'), ('Permanent', 'Permanent'), ('Probationary', 'Probationary'), ('Limited_term', 'Limited-term'), ('Temporary', 'Temporary')], max_length=15)),
                ('IsActive', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmpMgrDept',
            fields=[
                ('Emp_MgrDept_ID', models.PositiveIntegerField(default=0, primary_key=True, serialize=False)),
                ('Dept_ID', models.PositiveIntegerField(default=0)),
                ('Emp_FullName', models.CharField(max_length=50)),
                ('Dept_Name', models.CharField(max_length=30)),
                ('Manager_FullName', models.CharField(max_length=50)),
                ('Manager_Email_Address', models.EmailField(max_length=70)),
                ('Emp_No_EmpMgrDept', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Emp_No_EmpMgrDept', to='LMS.Employee')),
                ('Manager_Emp_ID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Manager_Emp_ID', to='LMS.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveBalance',
            fields=[
                ('LeaveBal_ID', models.PositiveIntegerField(default=0, primary_key=True, serialize=False)),
                ('Leave_Type', models.CharField(choices=[('Personal_Leave', 'Personal'), ('Annual_Leave', 'Annual'), ('Military_Leave', 'Military'), ('Pregnancy_Disability_Leave', 'PDL'), ('Pending_Status', 'Pending'), ('Approved_Status', 'Approved'), ('Declined_Status', 'Declined')], max_length=10)),
                ('Available_Days', models.PositiveIntegerField(default=0, help_text='Remaining/available leave days per employee')),
                ('Allocated_Days', models.PositiveIntegerField(default=0, help_text='No of leave days allocated to a leave type per employee per year')),
                ('Emp_No_LeaveBal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LMS.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='empleaverequest',
            name='Emp_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Emp_ID', to='LMS.Employee'),
        ),
        migrations.AddField(
            model_name='empleaverequest',
            name='Manager_Emp_No',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Manager_Emp_No', to='LMS.Employee'),
        ),
    ]
