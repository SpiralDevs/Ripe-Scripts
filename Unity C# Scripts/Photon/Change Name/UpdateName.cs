using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Photon.Pun;
using TMPro;

public class UpdateName : MonoBehaviour
{
    public TMP_InputField nameTF;

    void Update()
    {
        nameTF = PhotonNetwork.NickName;
    }
}