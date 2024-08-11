# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
%bcond_with check
%global debug_package %{nil}

%global crate erased-serde

Name:           rust-erased-serde
Version:        0.4.5
Release:        1
Summary:        Type-erased Serialize and Serializer traits
Group:          Development/Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/erased-serde
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  (crate(serde) >= 1.0.194 with crate(serde) < 2.0.0~)
BuildRequires:  (crate(serde/alloc) >= 1.0.194 with crate(serde/alloc) < 2.0.0~)
BuildRequires:  (crate(serde/std) >= 1.0.194 with crate(serde/std) < 2.0.0~)
BuildRequires:  (crate(typeid/default) >= 1.0.0 with crate(typeid/default) < 2.0.0~)
BuildRequires:  rust >= 1.61
%if %{with check}
BuildRequires:  (crate(rustversion/default) >= 1.0.13 with crate(rustversion/default) < 2.0.0~)
BuildRequires:  (crate(serde_cbor/default) >= 0.11.2 with crate(serde_cbor/default) < 0.12.0~)
BuildRequires:  (crate(serde_derive/default) >= 1.0.194 with crate(serde_derive/default) < 2.0.0~)
BuildRequires:  (crate(serde_json/default) >= 1.0.99 with crate(serde_json/default) < 2.0.0~)
BuildRequires:  (crate(trybuild/default) >= 1.0.83 with crate(trybuild/default) < 2.0.0~)
BuildRequires:  (crate(trybuild/diff) >= 1.0.83 with crate(trybuild/diff) < 2.0.0~)
%endif

%global _description %{expand:
Type-erased Serialize and Serializer traits.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(erased-serde) = 0.4.5
Requires:       (crate(serde) >= 1.0.194 with crate(serde) < 2.0.0~)
Requires:       (crate(typeid/default) >= 1.0.0 with crate(typeid/default) < 2.0.0~)
Requires:       cargo
Requires:       rust >= 1.61

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(erased-serde/default) = 0.4.5
Requires:       cargo
Requires:       crate(erased-serde) = 0.4.5
Requires:       crate(erased-serde/std) = 0.4.5

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(erased-serde/alloc) = 0.4.5
Requires:       (crate(serde/alloc) >= 1.0.194 with crate(serde/alloc) < 2.0.0~)
Requires:       cargo
Requires:       crate(erased-serde) = 0.4.5

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(erased-serde/std) = 0.4.5
Requires:       (crate(serde/std) >= 1.0.194 with crate(serde/std) < 2.0.0~)
Requires:       cargo
Requires:       crate(erased-serde) = 0.4.5
Requires:       crate(erased-serde/alloc) = 0.4.5

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable-debug-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(erased-serde/unstable-debug) = 0.4.5
Requires:       cargo
Requires:       crate(erased-serde) = 0.4.5

%description -n %{name}+unstable-debug-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable-debug" feature of the "%{crate}" crate.

%files       -n %{name}+unstable-debug-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
