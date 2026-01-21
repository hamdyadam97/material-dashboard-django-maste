from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, get_object_or_404
from .forms import BranchForm
from .models import Branch
from django.core.paginator import Paginator
from django.shortcuts import render


def is_admin(user):
    return user.is_superuser


@login_required
def branch_list(request):
    branches = Branch.objects.all()

    # CREATE / EDIT
    if request.method == 'POST':
        if not request.user.is_superuser:
            return redirect('branches:branch_list')

        branch_id = request.POST.get('branch_id')

        if branch_id:
            branch = get_object_or_404(Branch, id=branch_id)
            form = BranchForm(request.POST, instance=branch)
        else:
            form = BranchForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('branches:branch_list')

    else:
        form = BranchForm()  # 👈 ده المهم

    return render(request, 'branches/branch_list.html', {
        'branches': branches,
        'form': form
    })


@user_passes_test(is_admin)
def branch_delete(request, pk):
    branch = get_object_or_404(Branch, pk=pk)

    if request.method == 'POST':
        branch.delete()
        return redirect('branch_list')

    return render(request, 'branches/branch_confirm_delete.html', {
        'branch': branch
    })
